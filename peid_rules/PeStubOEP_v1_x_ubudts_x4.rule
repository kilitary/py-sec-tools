rule _PeStubOEP_v1_x_ubudts
{
	meta:
		description = "PeStubOEP v1_x"
	strings:
		$a = {????B8??????00FFE0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
