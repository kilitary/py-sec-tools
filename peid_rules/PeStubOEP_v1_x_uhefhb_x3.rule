rule _PeStubOEP_v1_x_uhefhb
{
	meta:
		description = "PeStubOEP v1_x"
	strings:
		$a = {E80500000033C04048C3E805}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
