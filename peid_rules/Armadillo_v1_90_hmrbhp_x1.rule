rule _Armadillo_v1_90_hmrbhp
{
	meta:
		description = "Armadillo v1_90"
	strings:
		$a = {558BEC6AFF6810F2400068649A400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
