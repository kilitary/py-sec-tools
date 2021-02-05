rule _Private_exe_Protector_2_15__SetiSoft_Team_vgesxd
{
	meta:
		description = "Private exe Protector 2_15 __ SetiSoft Team"
	strings:
		$a = {00000000000000000000000000????????????????00000000000000000000000000000000000000004B45524E454C33322E444C4C0000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
