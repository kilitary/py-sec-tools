rule _Armadillo_v2_52_cppkbx
{
	meta:
		description = "Armadillo v2_52"
	strings:
		$a = {558BEC6AFF68????????B0????????686064A100000000506489250000000083EC585356578965E8FF??????1524}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
