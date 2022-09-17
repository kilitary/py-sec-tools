rule _ASProtect_v1_2x_adyqbm
{
	meta:
		description = "ASProtect v1_2x"
	strings:
		$a = {00006801??????C3AA}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
