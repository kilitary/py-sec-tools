rule _Armadillo_v1_90b1_ocxqtz
{
	meta:
		description = "Armadillo v1_90b1"
	strings:
		$a = {558BEC6AFF68E0C14000680489400064A100000000506489250000000083EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
