rule _Armadillo_v1_82_axwobu
{
	meta:
		description = "Armadillo v1_82"
	strings:
		$a = {558BEC6AFF68E0C14000687481400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
