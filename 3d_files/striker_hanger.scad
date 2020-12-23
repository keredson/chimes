T = 1;

em_d = 20; // electromagnet
em_l = 30;

b_w = 25.4; //em_d + 2*T; // block
b_l = 50.8; //em_l + T + 17;
b_h = em_d + 2*T + 8;

r_d = 3.2; // 1/8" dowel
r_l = 150;

nail_d = 1.8; // 18ga brad

hanger_y_inset = 5;

difference() {
    union() {
        translate([-T,-T,-T]) cube([b_w+2*T,b_l+2*T,T]);
        cube([b_w,b_l,b_h]);
    }
    translate([b_w/2, -1, em_d/2]) rotate([-90,0,0]) cylinder(100, em_d/2, em_d/2, $fn=50);
    
    // hanger 
    for(d=[0:2:10]) {
        translate([b_w/2-r_d/2, b_l-hanger_y_inset, b_h]) rotate([-d,0,0])
        translate([0,0,-(b_h+r_l)]) cube([r_d, r_d, b_h+r_l]);
    }
    translate([b_w/2,b_l-hanger_y_inset+1,b_h-5]) union() {
        rotate([90,0,0]) translate([0,-3.2,-0]) cylinder(10,1.6,1.6, $fn=50);
        rotate([0,90,0]) translate([0,0,-4.2]) cylinder(8.4,1.1,1.1, $fn=50);
        translate([0,-1,0]) cube([r_d+1.5,r_d+4,20], center=true);
        translate([0,0,5]) cube([9,2.3,10], center=true);
    }
    
    // controller cutout
    translate([b_w/2,0,b_h]) union() {
        translate([0,10,0]) cube([b_w-2*T,b_l,12], center=true);
    }
    translate([b_w/2,0,b_h]) union() {
        translate([0,6,-7]) cube([b_w,12,14], center=true);
    }

    // wire hanger
    inset = 2.5;
    for(i=[inset, b_w-inset])
    translate([i,9.5,-T]) rotate([0,90,0])
    rotate_extrude(angle=360, $fa=1) {
     translate([4, 0])circle(d=3.5, $fs=0.4);
    }
    
    // screw holes
    for(i=[5,b_w-5])
    translate([i,b_l-10,-T]) union() {
        cylinder(100, 1, 1, $fn=20);
        translate([0,0,b_h-1]) cylinder(T, 2.5, 1, $fn=20);
        translate([0,0,0]) cylinder(b_h-1, 2.5, 2.5, $fn=20);
    }
    
    // nail holes
    /*
    for(i=[18, b_l-3]) for(j=[-1,1])
    translate([b_w/2 + j*5.5,i,-5.5])
    rotate([0,j*45,0])
    cylinder(40, nail_d/2, nail_d/2, $fn=10); //*/
    
}

