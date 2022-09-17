rule _Private_exe_Protector_2_0__SetiSoft_Team_ajzubv
{
	meta:
		description = "Private exe Protector 2_0 __ SetiSoft Team"
	strings:
		$a = {0000000000000000????????????????00000000000000000000000000000000000000004B45524E454C33322E444C4C00????????000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
