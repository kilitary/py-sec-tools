rule _Armadillo_v1_71_fxjbcb
{
	meta:
		description = "Armadillo v1_71"
	strings:
		$a = {558BEC6AFF68????????68????????64A1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
