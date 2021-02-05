rule _Armadillo_v1_83_ksmxgk
{
	meta:
		description = "Armadillo v1_83"
	strings:
		$a = {558BEC6AFF68E0C14000686484400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
