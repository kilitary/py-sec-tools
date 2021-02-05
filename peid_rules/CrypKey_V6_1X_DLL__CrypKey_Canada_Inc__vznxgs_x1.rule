rule _CrypKey_V6_1X_DLL__CrypKey_Canada_Inc__vznxgs
{
	meta:
		description = "CrypKey V6_1X DLL __ CrypKey _Canada_ Inc_"
	strings:
		$a = {833D????????00753468????????E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
