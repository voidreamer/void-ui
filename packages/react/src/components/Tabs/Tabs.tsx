import { forwardRef, type HTMLAttributes, type ReactNode } from 'react'
import { cn } from '../../utils'

export interface TabItem {
  /** Unique key for the tab */
  key: string
  /** Tab label */
  label: ReactNode
  /** Tab content */
  content?: ReactNode
}

export interface TabsProps extends Omit<HTMLAttributes<HTMLDivElement>, 'onChange'> {
  /** Tab items */
  items: TabItem[]
  /** Currently active tab key */
  activeKey?: string
  /** Called when tab changes */
  onChange?: (key: string) => void
}

export const Tabs = forwardRef<HTMLDivElement, TabsProps>(
  ({ items, activeKey, onChange, className, ...props }, ref) => {
    return (
      <div ref={ref} className={className} {...props}>
        <div className="void-tabs" role="tablist">
          {items.map((item) => (
            <button
              key={item.key}
              role="tab"
              aria-selected={activeKey === item.key}
              className={cn('void-tab', activeKey === item.key && 'void-tab--active')}
              onClick={() => onChange?.(item.key)}
            >
              {item.label}
            </button>
          ))}
        </div>
        {items.map((item) =>
          activeKey === item.key && item.content ? (
            <div key={item.key} role="tabpanel" style={{ marginTop: 'var(--space-lg, 1.5rem)' }}>
              {item.content}
            </div>
          ) : null
        )}
      </div>
    )
  }
)

Tabs.displayName = 'Tabs'
