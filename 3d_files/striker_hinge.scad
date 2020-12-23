T = 1;

em_d = 20; // electromagnet
em_l = 30;

b_w = em_d + 2*T; // block
b_l = em_l + T + 7;
b_h = em_d + 2*T + 5;

r_d = 3.6; // 1/8" dowel
r_l = 150;



translate([10,-10,0]) {
    difference() {
        union() {
            cylinder(4,r_d/2+.5,r_d/2+.5, $fn=50);
            rotate([0,90,0]) translate([0,0,-4]) cylinder(8,1,1, $fn=50);
        }
        cylinder(5,r_d/2,r_d/2, $fn=50);
        translate([0,0,3.5]) cylinder(.5,r_d/2,r_d/2+.5, $fn=50);
        translate([-10,-10,-20]) cube([20,20,20]);
    }
}