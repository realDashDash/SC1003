module vaddoflow(
    input [3:0] a,
    input [3:0] b,
    output [6:0] seg_L,
    output oflow
    );
    wire [4:0] x;
    assign x = a + b;
    vsevenseg sevenseg (.x(x[3:0]), .seg_L(seg_L[6:0]));
    assign oflow = x[4];
endmodule