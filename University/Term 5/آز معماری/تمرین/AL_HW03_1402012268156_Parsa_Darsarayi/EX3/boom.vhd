----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    21:25:03 10/19/2025 
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
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;


-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity boom is
	Port( S : in std_logic_vector( 2 downto 0);
			Q : out std_logic_vector(7 downto 0);
			E : in std_logic);
end boom;

architecture Behavioral of boom is

begin
		process(S,E)
			begin
				if E = '0' then
					Q <= "00000000";
				else
					case S is
						when "000" => Q <= "00000001";
						when "001" => Q <= "00000010";
						when "010" => Q <= "00000100";
						when "011" => Q <= "00001000";
						when "100" => Q <= "00010000";
						when "101" => Q <= "00100000";
						when "110" => Q <= "01000000";
						when "111" => Q <= "10000000";
						when others => null;
					end case;
				end if;
			end process;
end Behavioral;

