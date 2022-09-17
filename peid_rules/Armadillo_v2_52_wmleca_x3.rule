rule _Armadillo_v2_52_wmleca
{
	meta:
		description = "Armadillo v2_52"
	strings:
		$a = {558BEC6AFF68????????E0????????68D464A100000000506489250000000083EC585356578965E8FF??????1538}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
