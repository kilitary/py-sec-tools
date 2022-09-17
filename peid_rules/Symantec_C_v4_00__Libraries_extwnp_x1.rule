rule _Symantec_C_v4_00__Libraries_extwnp
{
	meta:
		description = "Symantec C v4_00 _ Libraries"
	strings:
		$a = {FAB8????DBE38ED88C06????8BD82B1E????891E????26}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
