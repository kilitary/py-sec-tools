rule _Vx_Compiler_klmejl
{
	meta:
		description = "Vx_ Compiler"
	strings:
		$a = {8CC383C3102E011E??022E031E??02531E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
