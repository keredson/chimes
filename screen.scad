T=2;
screen_w = 34;
screen_h = 12;
screen_d = 18;
screen_vis_h = 8;
screen_vis_w = 24;
screen_vis_offset_top = 1.5;
screen_vis_offset_left = 2;

outer_w = 46;
outer_h = 19;


x_middle = (outer_w-2*T)/2;
z_middle = (outer_h-T)/2;
echo(x_middle);
echo(z_middle);


difference() {
    union() {
        translate([-T,-T,-T]) cube([outer_w, screen_d+T+1, outer_h]);
    }
    cube([outer_w-2*T, screen_d, 100]);
//    #translate([
//        screen_w-screen_vis_w-screen_vis_offset_left, 
//        screen_d-1, 
//        screen_h-screen_vis_h-screen_vis_offset_top
//    ]) cube([screen_vis_w, 4, screen_vis_h]);
    
    translate([
        x_middle,
        screen_d+1,
        z_middle-1
    ]) cube([screen_vis_w, 4, screen_vis_h], center=true);

    translate([
        x_middle - (screen_w - screen_vis_w)/2 + screen_vis_offset_left,
        screen_d,
        z_middle-1 - (screen_h - screen_vis_h)/2 + screen_vis_offset_top
    ]) cube([screen_w, 1, screen_h], center=true);

    #translate([
        x_middle - (screen_w - screen_vis_w)/2 + screen_vis_offset_left,
        screen_d - (sqrt(2)-1),
        z_middle-1 - (-screen_vis_h)/2 + screen_vis_offset_top
    ]) rotate([45,0,0]) cube([screen_w, 1, 1], center=true);
}

difference() {
    union() {
        translate([x_middle,3.5,0]) cylinder(z_middle*2+T,4,4, $fn=20);
        cube([x_middle,5,z_middle*2]);
    }
    translate([x_middle,3.5,0]) cylinder(21,3,3, $fn=20);
    translate([x_middle+3,3.5,0]) cube([4,4,100], center=true);
}

