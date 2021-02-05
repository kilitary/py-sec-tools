rule _Armadillo_v2_00_kotvni
{
	meta:
		description = "Armadillo v2_00"
	strings:
		$a = {558BEC6AFF680002410068C4A0400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
