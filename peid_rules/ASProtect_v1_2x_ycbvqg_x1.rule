rule _ASProtect_v1_2x_ycbvqg
{
	meta:
		description = "ASProtect v1_2x"
	strings:
		$a = {6801??????E801??????C3C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
