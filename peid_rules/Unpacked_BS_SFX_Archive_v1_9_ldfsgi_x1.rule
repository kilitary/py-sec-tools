rule _Unpacked_BS_SFX_Archive_v1_9_ldfsgi
{
	meta:
		description = "Unpacked BS_SFX Archive v1_9"
	strings:
		$a = {1E33C050B8????8ED8FA8ED0BC????FBB8????CD213C0373}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
