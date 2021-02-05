rule _The_aPE_Inline_Patch_ExtraStealth_SuperStealth__mhqnni
{
	meta:
		description = "The aPE Inline Patch ExtraStealth_ SuperStealth_"
	strings:
		$a = {E802??????EB01C33E8B4424FC50B9????????E8????????89}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
