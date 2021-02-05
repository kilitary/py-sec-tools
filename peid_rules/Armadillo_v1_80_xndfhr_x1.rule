rule _Armadillo_v1_80_xndfhr
{
	meta:
		description = "Armadillo v1_80"
	strings:
		$a = {558BEC6AFF68E8C1000068F486000064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
