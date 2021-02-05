rule _Turbo_C_1987_dggpwd
{
	meta:
		description = "Turbo C 1987"
	strings:
		$a = {FBBA????2E89??????B430CD21}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
