rule _PeStubOEP_v1_x_lclqum
{
	meta:
		description = "PeStubOEP v1_x"
	strings:
		$a = {9033C933D2B8??????00B9FF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
