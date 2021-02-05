rule _Netopsystems_FEAD_Optimizer_xtlnel
{
	meta:
		description = "Netopsystems FEAD Optimizer"
	strings:
		$a = {60BE005043008DBE00C0FCFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
