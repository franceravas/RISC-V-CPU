module logic1 (
    input logic clk,
    input logic reset_n,
    input logic data_in,
    output logic data_out
);

always @(posedge clk) begin
    if(~reset_n) begin
        data_out <= 1'b0;
    end else begin
        data_out <= data_in;
    end
end
    
endmodule