library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity TB_Mux16x1 is
end TB_Mux16x1;

architecture behavior of TB_Mux16x1 is

    -- Component declaration
    component Mux16x1
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
    end component;

    signal I0,I1,I2,I3,I4,I5,I6,I7 : STD_LOGIC := '0';
    signal I8,I9,I10,I11,I12,I13,I14,I15 : STD_LOGIC := '0';
    signal S  : STD_LOGIC_VECTOR(3 downto 0) := (others=>'0');
    signal Y  : STD_LOGIC;

begin

    -- Instantiate the Unit Under Test (UUT)
    uut: Mux16x1 port map(
        I0=>I0,  I1=>I1,  I2=>I2,  I3=>I3,
        I4=>I4,  I5=>I5,  I6=>I6,  I7=>I7,
        I8=>I8,  I9=>I9,  I10=>I10, I11=>I11,
        I12=>I12,I13=>I13,I14=>I14,I15=>I15,
        S=>S, Y=>Y
    );

    -- Test process
    stim_proc: process
    begin

        -- Assign unique values to inputs
        I0 <= '0';  I1 <= '1';  I2 <= '0';  I3 <= '1';
        I4 <= '0';  I5 <= '1';  I6 <= '0';  I7 <= '1';
        I8 <= '0';  I9 <= '1';  I10 <= '0'; I11 <= '1';
        I12 <= '0'; I13 <= '1'; I14 <= '0'; I15 <= '1';

        -- Test all select values 0..15
        for i in 0 to 15 loop
            S <= std_logic_vector(to_unsigned(i,4));
            wait for 20 ns;
        end loop;

        wait;
    end process;

end behavior;