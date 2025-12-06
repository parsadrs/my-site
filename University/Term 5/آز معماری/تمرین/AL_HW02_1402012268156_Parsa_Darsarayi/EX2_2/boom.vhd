----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    21:41:53 10/19/2025 
-- Design Name: 
-- Module Name:    boom - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity boom is
	Port( S : in std_logic_vector( 4 downto 0);
			Q : out std_logic_vector(31 downto 0);
			E : in std_logic);
end boom;

architecture Behavioral of boom is

begin
		process(S,E)
			begin
				if E = '0' then
					Q <= "00000000000000000000000000000000";
				else
					case S is
						when "00000" => Q <= "00000000000000000000000000000001";
						when "00001" => Q <= "00000000000000000000000000000010";
						when "00010" => Q <= "00000000000000000000000000000100";
						when "00011" => Q <= "00000000000000000000000000001000";
						when "00100" => Q <= "00000000000000000000000000010000";
						when "00101" => Q <= "00000000000000000000000000100000";
						when "00110" => Q <= "00000000000000000000000001000000";
						when "00111" => Q <= "00000000000000000000000010000000";
						when "01000" => Q <= "00000000000000000000000100000000";
						when "01001" => Q <= "00000000000000000000001000000000";
						when "01010" => Q <= "00000000000000000000010000000000";
						when "01011" => Q <= "00000000000000000000100000000000";
						when "01100" => Q <= "00000000000000000001000000000000";
						when "01101" => Q <= "00000000000000000010000000000000";
						when "01110" => Q <= "00000000000000000100000000000000";
						when "01111" => Q <= "00000000000000001000000000000000";
						when "10000" => Q <= "00000000000000010000000000000000";
						when "10001" => Q <= "00000000000000100000000000000000";
						when "10010" => Q <= "00000000000001000000000000000000";
						when "10011" => Q <= "00000000000010000000000000000000";
						when "10100" => Q <= "00000000000100000000000000000000";
						when "10101" => Q <= "00000000001000000000000000000000";
						when "10110" => Q <= "00000000010000000000000000000000";
						when "10111" => Q <= "00000000100000000000000000000000";
						when "11000" => Q <= "00000001000000000000000000000000";
						when "11001" => Q <= "00000010000000000000000000000000";
						when "11010" => Q <= "00000100000000000000000000000000";
						when "11011" => Q <= "00001000000000000000000000000000";
						when "11100" => Q <= "00010000000000000000000000000000";
						when "11101" => Q <= "00100000000000000000000000000000";
						when "11110" => Q <= "01000000000000000000000000000000";
						when "11111" => Q <= "10000000000000000000000000000000";
						when others => null;
					end case;
				end if;
			end process;
end Behavioral;