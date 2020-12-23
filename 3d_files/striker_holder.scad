T = 1;

em_d = 20; // electromagnet
em_l = 30;

b_w = em_d + 2*T; // block
b_l = em_l + T + 7;
b_h = em_d + 2*T + 0;

r_d = 2; // rod, +1 for .5mm clearance each side
r_l = 150;

difference() {
    union() {
        translate([-T,-T,-T]) cube([b_w+2*T,b_l+2*T,T]);
        cube([b_w,b_l,b_h]);
    }
    translate([b_w/2, -1, em_d/2]) rotate([-90,0,0]) cylinder(100, em_d/2, em_d/2, $fn=50);
    
    for(d=[0:2:10]) {
        translate([b_w/2-r_d/2, em_l, b_h-1]) rotate([d,0,0])
        translate([0,0,-(b_h+r_l)]) cube([r_d, r_d, b_h+r_l]);
    }
}