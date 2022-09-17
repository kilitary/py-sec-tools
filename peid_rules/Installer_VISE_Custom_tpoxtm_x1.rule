rule _Installer_VISE_Custom_tpoxtm
{
	meta:
		description = "Installer VISE Custom"
	strings:
		$a = {558BEC6AFF68????400068????400064A100000000506489250000000083EC585356578965E8FF15????400033D28AD48915????40008BC881E1FF000000890D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
