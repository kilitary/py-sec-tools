rule _InstallShield_Cabinet_Archive_dtyrqc
{
	meta:
		description = "InstallShield Cabinet Archive"
	strings:
		$a = {495363}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
