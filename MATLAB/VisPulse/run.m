% Script to run the VisPulse on multiple CSV files
a = dir('*.csv')

for i=1:length(a),
	res = findstr('.',a(i).name)
	dname = genvarname(a(i).name(1:res(1)-1))
	eval([dname ' = importdata(a(i).name)'])
	eval(['mxRes = getPulse2(' dname ');'])
	eval(['save data_'  dname 'mxRes'])
	figH = figure('visible','off') ; 
	clf
	plot([mxRes.X mxRes.xHat mxRes.xPhi mxRes.X-mxRes.xHat-2],'.-')
	saveas(figH, sprintf('%s.png', dname));
	close(figH) ; 
end


% Script to run the VisPulse on multiple CSV files
a = dir('*.csv')

for i=1:2,
	res = findstr('.',a(i).name)
	dname = genvarname(a(i).name(1:res(1)-1))
	eval([dname ' = importdata(a(i).name)'])
	eval(['mxRes = getPulse2(' dname ');'])
	eval(['save data_'  dname 'mxRes'])
	figH = figure('visible','off') ; 
	clf
	plot([mxRes.X mxRes.xHat mxRes.xPhi mxRes.X-mxRes.xHat-2],'.-')
	saveas(figH, sprintf('%s.png', dname));
	close(figH) ; 
end

% Script to run the VisPulse on multiple CSV files
a = dir('*.csv')
for i=2:length(a),
	res = findstr('.',a(i).name)
	dname = genvarname(a(i).name(1:res(1)-1))
	eval([dname ' = importdata(a(i).name)'])
	eval(['mxRes = getPulse2(' dname ');'])
	eval(['save data_'  dname 'mxRes'])
	figH = figure('visible','off') ; 
	clf
	plot([mxRes.X mxRes.xHat mxRes.xPhi mxRes.X-mxRes.xHat-2],'.-')
	saveas(figH, sprintf('%s.png', dname));
	close(figH) ; 
end