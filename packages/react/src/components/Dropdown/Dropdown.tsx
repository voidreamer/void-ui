import { forwardRef, useState, useRef, useEffect, type HTMLAttributes, type ReactNode } from 'react'
import { cn } from '../../utils'

export interface DropdownItem {
  /** Unique key */
  key: string
  /** Item label */
  label: ReactNode
  /** Danger styling */
  danger?: boolean
  /** Separator before this item */
  separator?: boolean
}

export interface DropdownProps extends Omit<HTMLAttributes<HTMLDivElement>, 'onSelect'> {
  /** Dropdown trigger element */
  trigger: ReactNode
  /** Menu items */
  items: DropdownItem[]
  /** Called when an item is selected */
  onSelect?: (key: string) => void
  children?: ReactNode
}

export const Dropdown = forwardRef<HTMLDivElement, DropdownProps>(
  ({ trigger, items, onSelect, className, ...props }, ref) => {
    const [open, setOpen] = useState(false)
    const wrapRef = useRef<HTMLDivElement>(null)

    useEffect(() => {
      const handler = (e: MouseEvent) => {
        if (wrapRef.current && !wrapRef.current.contains(e.target as Node)) {
          setOpen(false)
        }
      }
      document.addEventListener('mousedown', handler)
      return () => document.removeEventListener('mousedown', handler)
    }, [])

    return (
      <div
        ref={wrapRef}
        className={cn('void-dropdown', open && 'void-dropdown--open', className)}
        {...props}
      >
        <div onClick={() => setOpen(!open)}>{trigger}</div>
        <div className="void-dropdown__menu">
          {items.map((item) => (
            <div key={item.key}>
              {item.separator && <div className="void-dropdown__sep" />}
              <button
                className={cn('void-dropdown__item', item.danger && 'void-dropdown__item--danger')}
                onClick={() => {
                  onSelect?.(item.key)
                  setOpen(false)
                }}
              >
                {item.label}
              </button>
            </div>
          ))}
        </div>
      </div>
    )
  }
)

Dropdown.displayName = 'Dropdown'
