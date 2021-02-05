rule _Armadillo_v1_90c_rkidma
{
	meta:
		description = "Armadillo v1_90c"
	strings:
		$a = {558BEC6AFF6810F2400068749D400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
