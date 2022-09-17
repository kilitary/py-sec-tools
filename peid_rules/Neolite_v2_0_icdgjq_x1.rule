rule _Neolite_v2_0_icdgjq
{
	meta:
		description = "Neolite v2_0"
	strings:
		$a = {E9A6000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
