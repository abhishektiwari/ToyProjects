function out = AICc(n,K,ssqResidual)
	
out=real(log(ssqResidual/(n-K))+(n+K)/(n-K-2));
