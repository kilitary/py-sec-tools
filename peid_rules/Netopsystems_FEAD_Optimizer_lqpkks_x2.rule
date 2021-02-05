rule _Netopsystems_FEAD_Optimizer_lqpkks
{
	meta:
		description = "Netopsystems FEAD Optimizer"
	strings:
		$a = {E80000000058BB000040008B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
