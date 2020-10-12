set i /0*14/;
set j /0*204/;

parameter d(j,*)
$call gdxxrw.exe ResultsSFLP.xlsx par=d rng=Sheet1!a1 rdim=1 cdim =1
$gdxin ResultsSFLP.gdx
$load d
display d
parameter c(j);
c(j)=d(j,'2');

parameter ch(i,j)
$call gdxxrw.exe convexhull.xlsx par=ch rng=Sheet1!a1 rdim=1 cdim =1
$gdxin convexhull.gdx
$load ch
display ch

scalar f /3/;


binary variable t(j);

variable z;

equations
obj,
facility,
cover(i);

obj.. z =e= sum(j,t(j)*c(j));
facility.. sum(j,t(j)) =e= f;
cover(i).. sum(j$(ch(i,j)=1),t(j)) =g= 1;

model setcover  /all/ ;

solve setcover using mip min z;


execute_unload "hull.gdx", t.l,z.l
execute 'gdxxrw.exe hull.gdx  var=t rng=Sheet1!a1'
execute 'gdxxrw.exe hull.gdx  var=z rng=Sheet2!a1'
