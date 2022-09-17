rule _PeStubOEP_v1_x_mruymh
{
	meta:
		description = "PeStubOEP v1_x"
	strings:
		$a = {4048BE00????0040486033C0B8??????00FFE0C3C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
