library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Mux16x1 is
    Port(
        I0  : in  STD_LOGIC;
        I1  : in  STD_LOGIC;
        I2  : in  STD_LOGIC;
        I3  : in  STD_LOGIC;
        I4  : in  STD_LOGIC;
        I5  : in  STD_LOGIC;
        I6  : in  STD_LOGIC;
        I7  : in  STD_LOGIC;
        I8  : in  STD_LOGIC;
        I9  : in  STD_LOGIC;
        I10 : in  STD_LOGIC;
        I11 : in  STD_LOGIC;
        I12 : in  STD_LOGIC;
        I13 : in  STD_LOGIC;
        I14 : in  STD_LOGIC;
        I15 : in  STD_LOGIC;
        S   : in  STD_LOGIC_VECTOR(3 downto 0);
        Y   : out STD_LOGIC
    );
end Mux16x1;

architecture Behavioral of Mux16x1 is
begin
    process(I0,I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,I14,I15, S)
    begin
        case S is
            when "0000" => Y <= I0;
            when "0001" => Y <= I1;
            when "0010" => Y <= I2;
            when "0011" => Y <= I3;
            when "0100" => Y <= I4;
            when "0101" => Y <= I5;
            when "0110" => Y <= I6;
            when "0111" => Y <= I7;
            when "1000" => Y <= I8;
            when "1001" => Y <= I9;
            when "1010" => Y <= I10;
            when "1011" => Y <= I11;
            when "1100" => Y <= I12;
            when "1101" => Y <= I13;
            when "1110" => Y <= I14;
            when "1111" => Y <= I15;
            when others => Y <= '0';
        end case;
    end process;
end Behavioral;