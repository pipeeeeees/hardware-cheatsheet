  module adder(
      input [7:0] a,
      input [7:0] b,
      output reg [7:0] sum
  );

  always @(a or b) begin
      sum = a + b;
  end

  endmodule