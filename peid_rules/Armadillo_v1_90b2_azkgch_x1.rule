rule _Armadillo_v1_90b2_azkgch
{
	meta:
		description = "Armadillo v1_90b2"
	strings:
		$a = {558BEC6AFF68F0C1400068A489400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
