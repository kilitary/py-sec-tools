rule _Armadillo_v2_00b2_2_00b3_nasbvv
{
	meta:
		description = "Armadillo v2_00b2_2_00b3"
	strings:
		$a = {558BEC6AFF6800F2400068C4A0400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
