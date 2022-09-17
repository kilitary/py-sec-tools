rule _Armadillo_v1_90b4_gjhyzn
{
	meta:
		description = "Armadillo v1_90b4"
	strings:
		$a = {558BEC6AFF6808E2400068B496400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
