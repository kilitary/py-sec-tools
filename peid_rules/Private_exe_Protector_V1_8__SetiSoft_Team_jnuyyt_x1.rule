rule _Private_exe_Protector_V1_8__SetiSoft_Team_jnuyyt
{
	meta:
		description = "Private exe Protector V1_8 __ SetiSoft Team"
	strings:
		$a = {00000000000000000000000000000000000000004B45524E454C33322E444C4C00????????0000000000004578697450726F63657373}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
