function [F] = getPulseFun(vecIn,X,lambda,k1,k2,alpha,idxPhi,basal,iMode)
if(iMode ==1)
	k2=vecIn(1);
	phi = vecIn((1:145)+1);
elseif(iMode ==2)
	phi = zeros(145,1);
	basal = vecIn(1);
	phi(idxPhi) = vecIn(2:length(idxPhi)+1);
elseif(iMode == 3)
	phi = zeros(145,1);
	basal = vecIn(1);
	phi(idxPhi) = vecIn(2:length(idxPhi)+1);
else
	disp('serious issues, scripts cannot run in this configuration');
	F=0;
	return;
end

idx=1:145;
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

phi2=zeros(145,1);
iQuant = quantile(phi,lambda);
idx = find(phi <= iQuant);
phi2(idx)=phi(idx);
n=145;
K=length(find(phi>0.1));
n=145;
K=length(idxPhi)+3;
%  AIC = n*log(var(X-Xhat))+2*K*(n/(n-K-1)) ; 
% F=[(X-Xhat)';5*max(X)*phi2;max(X)*tanh(real(sqrt(AIC)));max(X)*tanh(imag(sqrt(AIC)))+1];
% disp(sprintf('Residual: %.3f, penalty %.3f',ssq(X-Xhat),ssq(5*max(X)*phi2)));
F=[(X-Xhat)';5*max(X)*phi2];
%  F=[(X-Xhat)'];

% disp(sprintf('ssq: %.5e, aicc: %.8e',ssq(X-Xhat),AIC));

function out = funDecayInline(alpha,k1,k2,t)
out=(alpha*exp(k1*t)+(1-alpha)*exp(k2*t));
if(out>1)
	disp('panic');
end
