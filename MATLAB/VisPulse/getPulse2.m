function [mxRes] = getPulse(X,k1,k2,alpha, phi,basal)
% k is rate constant, phi is peak/pulse profile, phi is zero or higher
% usage option 1:
% [mxRes] = getPulse(X);
% usage optioin 2:
% [mxRes] = getPulse(X, k1, k2, alpha, phi); 
iMode = 0;
if (nargin==1)
%	options=optimset('TolFun',1e-9,'Jacobian','off','LargeScale','on', 'MaxFunEvals',15000, 'MaxIter',200000, 'Display','off');
    options=optimset('TolFun',1e-9,'Jacobian','off','LargeScale','on', 'MaxFunEvals',15000, 'MaxIter',200000, 'Display','off');
	if(options.MaxFunEvals < 50000)
		disp('setting for maxfunevals in mode 1 is too low');
	end 
	iMaxLoop = 12;
	iMode = 1;
	phi = [];
elseif(nargin==5)
	options=optimset('TolFun',1e-9,'Jacobian','off','LargeScale','on', 'MaxFunEvals',15000, 'MaxIter',200000);
	iMaxLoop = 1;
	iMode = 2;
	basal=0;
elseif(nargin==6)
	options=optimset('TolFun',1e-5,'Jacobian','off','LargeScale','on', 'MaxFunEvals',15000, 'MaxIter',200000);
	iMaxLoop = 1;
	basal=0;
	iMode = 3;
else
	disp('Check your arguments to the function getPulse.m, it appears that you use this function against its specifications');
end

% start probing boundaries, middle and middles of the middle points (5
% point start)

vStart = [1 15 24 32 38 48];
% vStart = [48 38 32 24 15 1];
iMaxLoop = length(vStart);
vIdx = vStart;
bFirstScreening = true;
bRun = true;
q = 1;
iCnt = 1;
tic;
while(bRun)
		lambda=(83+vIdx(q))/145;
		xdiff=diff(X',1); %#ok<UDIM>
		xdiff(find(xdiff<quantile(xdiff,140/145)))=0;
		xdiff = [0 xdiff ];
%    		xdiff=diff(X',1); %#ok<UDIM>
%    		xdiff(find(xdiff<0))=0;
%    		xdiff = [0 xdiff ];
		
		if(iMode == 1)
			minVec = [-3.4;zeros(145,1)];
			maxVec = [-0.001;max(X)*ones(145,1)];
			k2=log(0.5)/6;
			k1=0;
			alpha=0;
			basal=0;
			idxPhi = 1:145;
			vecIn = [k2 xdiff]';
		elseif(iMode == 2)
			idxPhi = find(phi>0.001);
			vecIn = [0 phi(idxPhi)]';% -0.047104952716049
			
			minVec = [zeros(length(idxPhi),1)];
			maxVec = [10000*ones(length(idxPhi),1)];
		else
			disp('This should not happen');
			mxRes = [];
			return;
		end

		vecOut = lsqnonlin(@getPulseFun,vecIn,minVec,maxVec,options,X',lambda,k1,k2,alpha,idxPhi,basal,iMode);

		if (iMode == 1)
			k2 = vecOut(1);
			phi = vecOut((1:145)+1);
		elseif(iMode ==2)
			phi = zeros(145,1);
			phi(idxPhi) = vecOut(2:length(idxPhi)+1);
		elseif(iMode ==3)
			phi = zeros(145,1);
			basal = vecOut(1);
			phi(idxPhi) = vecOut(2:length(idxPhi)+1);
		end

		Xhat(1) = X(1);
		idx=1:145;
		mxSecrDecay = zeros(length(idx),145);
		phi0=X(1)/exp(k2);
		for(i=1:145)
			mxSecrDecay(1,i) = ((basal/exp(k2))+phi0)*funDecayInline(0,k1,k2,i);
		end
		for(j=2:145)
			for(i=j:145)
				mxSecrDecay(j,i) = (basal+phi(j))*funDecayInline(alpha,k1,k2,i-j);
			end
		end
		Xhat(1:145) = sum(mxSecrDecay);
		mxRes.xHat(iCnt,:) = Xhat;
		mxRes.xPhi(iCnt,:) = phi;
		mxRes.alpha(iCnt,:) = alpha;
		mxRes.k1(iCnt,:)=k1;
		mxRes.k2(iCnt,:)=k2;
		mxRes.xPhiInit(iCnt,:) = xdiff;
		mxRes.basal = basal;
		K=length(find(mxRes.xPhi(iCnt,:)>0.01));
		if(alpha>0)
			K=K+2;
		end
		n=145;
		K=K+1;
		AIC=AICc(n,K,ssq(X-mxRes.xHat(iCnt,:)'));
		disp(sprintf('alpha is %.2f - RSSQ is %.3f (k1=%.4f;k2=%.4f) - q %d - AIC: %.12e', alpha, ssq(X'-Xhat),10*log(0.5)/k1,10*log(0.5)/k2,q,AIC));
		mxRes.res(iCnt)=ssq(X'-Xhat);
		mxRes.AIC(iCnt)=AIC;
		if((q==iMaxLoop) && (bFirstScreening))
			minAIC=find(mxRes.AIC == min(mxRes.AIC));
			disp(sprintf('minimum near %d pulses- performing fine grained search',145-(vIdx(minAIC)+70)));
			if(minAIC == iMaxLoop)
				vIdx = vStart(minAIC-1)+1:vStart(minAIC)-1;
				iMaxLoop = length(vIdx);
				q=0;
			else
				vIdx = vStart(minAIC-1)+1:vStart(minAIC+1)-1;
				vIdx(vStart(minAIC)-vStart(minAIC-1))=[];
				iMaxLoop = length(vIdx);
				q=0;
			end
			bFirstScreening=false;
		end

		q=q+1;
		iCnt = iCnt +1;
		if((q>iMaxLoop) && (~bFirstScreening))
			bRun=false;
			minAIC=find(mxRes.AIC == min(mxRes.AIC));
			vCombi=[vStart vIdx];
			disp(sprintf('minimum near %d pulses - AIC of choice %.4e',145-(vCombi(minAIC)+70),mxRes.AIC(minAIC)));
			plot(145-(vCombi+70),mxRes.AIC,'.');
			mxOutRes = [];
			mxOutRes.mxRes=mxRes;
			mxOutRes.X=X;
			mxOutRes.xHat = mxRes.xHat(minAIC,:)';
			mxOutRes.xPhi = mxRes.xPhi(minAIC,:)';
			mxOutRes.k1 = mxRes.k1(minAIC);	
			mxOutRes.k2 = mxRes.k2(minAIC);
			disp(sprintf('to plot the results, use:\n plot([mxRes.X mxRes.xHat mxRes.xPhi])'));
		end
end

mxRes = mxOutRes;
toc;	

function out = funDecayInline(alpha,k1,k2,t)

out=(alpha*exp(k1*t)+(1-alpha)*exp(k2*t));

if(out>1)
	disp('panic');
end
