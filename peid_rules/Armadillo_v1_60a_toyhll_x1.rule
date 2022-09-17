rule _Armadillo_v1_60a_toyhll
{
	meta:
		description = "Armadillo v1_60a"
	strings:
		$a = {558BEC6AFF689871400068482D400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
