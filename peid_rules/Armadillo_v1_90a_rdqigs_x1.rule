rule _Armadillo_v1_90a_rdqigs
{
	meta:
		description = "Armadillo v1_90a"
	strings:
		$a = {558BEC64FF6810F2400068149B400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
