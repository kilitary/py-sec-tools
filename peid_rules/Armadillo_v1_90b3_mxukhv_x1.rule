rule _Armadillo_v1_90b3_mxukhv
{
	meta:
		description = "Armadillo v1_90b3"
	strings:
		$a = {558BEC6AFF6808E24000689495400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
