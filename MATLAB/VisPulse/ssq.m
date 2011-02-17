function [ssqRes]=ssq(X)
% calculates sum of squares of X

ssqRes=sum(sum(X.^2));