rule _Warning_may_be_SimbyOZ_polycryptor_by_3xpl01t_ver_2_xx_25_03_2007_22_00__sdgplj
{
	meta:
		description = "Warning_ may be SimbyOZ polycryptor by 3xpl01t ver 2_xx _25_03_2007 22_00_"
	strings:
		$a = {57578D7C240450B800D01713AB585FC30000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
